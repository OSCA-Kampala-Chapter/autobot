# autobot
![autobot-logo](./res/autobot.png)

Autobot is a bot library targetted to build software bots for various platforms with ease of integration in mind.
project still under active construction, so there's no proper documentation or support information to help that much. 
To contribute to the project, please follow along with the issues being posted and also the discussions.
### **The Basics**
> First off, thanks for taking the time to paticipate/contribute! :rocket: 

If you are looking to help you with a code contribution, this project uses [MKDocs](https://www.mkdocs.org/) for documentation generation, [Python](https://www.python.org/) for the writing the project code along with a splattering of [Markdown](https://www.markdownguide.org/) and [yaml](https://yaml.org/).  I've included our [VSCode](https://code.visualstudio.com/) workspace.  Read about [how I develop using VSCode](https://www.allisonthackston.com/articles/docker-development.html). If you don't feel ready to make autobot code contribution yet, no problem! You can also check out the issues we have in the [Github issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues)

#### **You want to contribute?**
Never made an open-source contribution before? Wondering how contributions work in this project? Here's a quick rundown![contribution-guide](/CONTRIBUTING.md) file for detailed contributing guidelines.

### Autobot
Autobot is an evolving python framework. It was originally designed to be a framework that enables the developer build bot systems for various platforms, with telegram being the first platform to be supported, but is now evolving into a fully functional automation and workflow engine that will help the developer build fully autonomous projects that react to events and also run timely scheduled tasks.
Autobot is in current transition to that automation framework, and currently there are bugs almost every, so the autobot team encourages you to report any bugs you encounter while testing out this framework. That being said, it's evident that autobot is not yet ready for production use, so please do not use it in your production projects.

#### Installation
In order to test out autobot, you have to first install it, and installing it is as easy as pip install. You can copy the snippet below into your command shell and run it.
```
pip install https://github.com/OSCA-Kampala-Chapter/autobot/archive/refs/tags/autobot-0.0.1a1.zip
```

#### Usage
Autobot has two seemingly independent components, and which can actually be used independently of each other. The first is the event system and the second is the bot layer. There is also the network abstraction layer but not really complicated. Let's talk about the event system first.

##### event system
The event system is an asynchronous event-driven component that tries to implement the actor model of concurrency. It offers a simple interface to register and run callbacks in response to events. The callbacks are simple asynchronous functions that take in an event as a parameter. The most import components of the event system right now are the `Event` and `EventDispatcher`. An event is implemented as a simple class with two attributes, `event_type` and `event_value`. The event dispatcher on the other hand is quite complex. It handles registering of events and their callbacks and triggers their execution once it receives an event. Let's try out a quick example, we shall write a simple program that reads a list of integer values and passes odd numbers to an odd-number-handler and an even number to an even-number-handler
```python
import asyncio
from autobot.events import Event
from autobot.events.dispatcher import EventDispatcher

ed:EventDispatcher = EventDispatcher() #instantiate the event dispatcher

@ed.add_handler("odds")
async def odd_handler(evt:Event) -> None:
    print(f"odd number {evt.event_value} handled")

@ed.add_handler("odds")
async def even_handler(evt:Event) -> None:
    print(f"even number {evt.event_value} handled")
    
async def main ():
    nums = [n for n in range(20)]
    for num in nums:
        if (num%2):
            ev = Event("odds",num)
            await ed.dispatch(ev)
        else:
            ev = Event("evens",num)
            await ed.dispatch(ev)
            
asyncio.run(main())
```
The expected output in interleaving prints such as "even number 0 handled" and "odd number 1 handled"
Let's digest this program simply. 
We have imported `Event` and `EventDispatcher` from the events submodule. Basically an event is the message and the event dispatcher is the messenger.
so we create an instance of the dispatcher and use the `add_handler`decorator to register async functions to handle the events. Think of these handlers as the recipients of the message and they are called by the messenger every time it receives a message that the recipients are interested in.

Well, here we tested a case where there is only one handler for one event. How about a case where there are multiple handlers or listeners for a single event. Let's modify the program so we can have 3 functions to handle odd numbers and 2 functions to handle even numbers.
```python
import asyncio
from autobot.events import Event
from autobot.events.dispatcher import EventDispatcher

ed:EventDispatcher = EventDispatcher()
@ed.add_handler("odds")
async def odd_handler1(evt:Event) -> None:
    print(f"first odd handler, handling {evt.event_value}")
    
@ed.add_handler("odds")
async def odd_handler2(evt:Event) -> None:
    print(f"second odd handler, handling {evt.event_value}")
    
@ed.add_handler("odds")
async def odd_handler3(evt:Event) -> None:
    print(f"third odd handler, handling {evt.event_value}")
    
@ed.add_handler("evens")
async def even_handler1(evt:Event) -> None:
    print(f"first even handler, handling {evt.event_value}")
    
@ed.add_handler("evens")
async def even_handler2(evt:Event) -> None:
    print(f"second even handler, handling {evt.event_value}")
    
async def main ():
    nums = [n for n in range(20)]
    for num in nums:
        if (num%2):
            ev = Event("odds",num)
            await ed.dispatch(ev)
        else:
            ev = Event("evens",num)
            await ed.dispatch(ev)
            
asyncio.run(main())
```
what you'll get again are interleaving prints. The callbacks are called in order of which they were added to the dispatcher.
This is mainly it concerning the event system.

##### bot layer
The currently supported bot platform is telegram. The bot layer provides a thin pythonic layer over the telegram API. So familiarity with the telegram bot api is important before using this wrapper. The telegram bot api is documented [here](https://core.telegram.org/bots/api)

First thing you need to do is create a bot account and get it's token. For details on how to do that, you can read [here](https://core.telegram.org/bots#how-do-i-create-a-bot).
After getting you token, you can now use autobot to interact with your telegram bot. Here's how, let's make a simple echo program that echos back to the sender the message they've sent to us
```python
import asyncio
from autobot.telegram.context import Context

token = "fill in the token here"
async def main ():
    cxt = Context(token)
    updates = await cxt.get_updates()
    for update in updates:
        if (m := update.message):
            cid = m.chat.id
            txt = m.text
            print(m.text)
            await cxt.send_message(chat_id = cid, text = txt)
            
asyncio.run(main())
```
**Note: known issue where an error is raised immediately after receiving and printing**

The Context is your entry point into the bot. It encapsulates the network and methods to interact with the bot. the `get_updates` method is a mirror to the `getUpdates` method of the telegram bot, and it accepts all arguments that can be passed to that of the telegram bot. An Update object is returned which has the same attributes as those listed on the bot api page under objects. You can access any of its attrbiutes via a dot operator, in this case we accessed the message object, which also has it's attributes as shown on the telegram bot api page, and it's atrributes can also be accessed via the dot operator. So we access it's text attribute and print it out. one of the attributes to the message object is the `chat` which also has an `id` attribute that represents the message sender. We extract that id and save it as `cid`, we also get the text from the message and save it as txt.
Using the send_message method, we send the message we received back to the sender

There's more that hasn't been documented yet, but the documentation is a work in progress, and we shall be updating the readme with relevant details as well, so keep in touch.
You're encouraged to ask all the questions on our github discussions as the documentation is being worked on.
