import json
from urllib.request import urlopen
import sys,os
sys.path.append(os.getcwd())

from autobot.telegram.games import *
from autobot.telegram.games import __all__ as game_all
from autobot.telegram.inline import *
from autobot.telegram.inline import __all__ as inline_all
from autobot.telegram.objects import *
from autobot.telegram.objects import __all__ as gen_all
from autobot.telegram.passport import *
from autobot.telegram.passport import __all__ as pass_all
from autobot.telegram.payments import *
from autobot.telegram.payments import __all__ as pay_all
from autobot.telegram.stickers import *
from autobot.telegram.stickers import __all__ as stick_all

all_objs = gen_all + game_all + inline_all + pass_all + pay_all + stick_all

resp = urlopen("https://raw.githubusercontent.com/PaulSonOfLars/telegram-bot-api-spec/main/api.json")
json_str = bytes(resp.read()).decode()
bot_objects = json.loads(json_str)
bot_types = bot_objects.pop("types")

scanned_objs = []


class TestInstances:
    fail = False

    def test_all_objects (self):
        missing_objs = []
        objs_missing_args = []
        cnt = 0

        for gen_obj in all_objs:
            print(f"  {cnt}  ".center(80,"="))
            print(f"scanning {gen_obj}".center(80))
            missing_args = []
            try:
                obj = eval(gen_obj+"()")
                bot_obj = bot_types[gen_obj]
                try:
                    for bot_field in bot_obj["fields"]:
                        attr = bot_field["name"]
                        print(f"found {attr}")

                        # quick fix
                        if not hasattr(obj,attr):
                            if attr == "from":
                                pass
                            else:
                                missing_args.append(attr)

                        setattr(obj,attr,None) # this is not supposed to assign attributes not in __slots__, but it does.

                except AttributeError:
                    if (attr == "from"):
                        print("found from")
                        setattr(obj,"from_",None)
                    else:
                        missing_args.append(attr)
            except KeyError as ke:
                if ke.args[0] == "BaseObject":
                    print("ignoring base object...")
                else:
                    missing_objs.append((cnt,gen_obj))
            
            finally:
                if len(missing_args):
                    for missing in missing_args:
                        print(f"  missing {missing}  ".center(80,"X"))
                    objs_missing_args.append((cnt,gen_obj))

                if objs_missing_args or missing_objs:
                    self.fail = True

            scanned_objs.append(gen_obj)
            cnt += 1

        print("\n\n\n  REPORT  ".center(80),end = "\n\n")
        print("  objects missing arguments ".center(80,"#"),end = "\n\n")
        for i in objs_missing_args:
            print(i)

        print("   missing telegram objects but exist in the library  ".center(80,"#"),end="\n\n")
        for i in missing_objs:
            print(i)

        print("   Missing objects in the bot api   ".center(80,"#"),end = "\n\n")
        for i in bot_types:
            if i not in scanned_objs:
                print(i)

if __name__ == "__main__":
    test = TestInstances()
    test.test_all_objects()
    if test.fail:
        sys.exit(1)
