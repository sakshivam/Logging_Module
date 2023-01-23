Python Logging:

The Python standard library comes with a logging module that provides most of the basic logging 
features. By setting it up correctly, a log message can bring a lot of useful information about 
when and where the log is fired as well as the log context, such as the running process/thread.

For logging, we should import logging library:
import logging

PYTHON LOGGING LEVELS

There are six log levels in Python; each level is associated with an integer that indicates the 
log severity: NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50.

PYTHON LOGGING FORMATTING
The log formatter basically enriches a log message by adding context information to it. It can be 
useful to know when the log is sent, where (Python file, line number, method, etc.), and additional 
context such as the thread and process (can be extremely useful when debugging a multithreaded 
application).

e.g.
logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s \t L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

Here fmt defines the format for printing log.

PYTHON LOGGING HANDLER
The log handler is the component that effectively writes/displays a log: Display it in the console 
(via StreamHandler), in a file (via FileHandler), or even by sending you an email via SMTPHandler, etc.

Each log handler has 2 important fields:

1. A formatter which adds context information to a log.
2. A log level that filters out logs whose levels are inferior. So a log handler with the INFO level will not
   handle DEBUG logs.

The most common ones are StreamHandler and FileHandler:
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("filename")

A new logger can be obtained by:
my_logger = logging.getLogger("test")

A logger has three main fields:

Propagate: Decides whether a log should be propagated to the logger’s parent. By default, its value is True.

A level: Like the log handler level, the logger level is used to filter out “less important” logs. Except, 
unlike the log handler, the level is only checked at the “child” logger; once the log is propagated to its 
parents, the level will not be checked. This is rather an un-intuitive behavior.

Handlers: The list of handlers that a log will be sent to when it arrives to a logger. This allows a flexible
 log handling—for example, you can have a file log handler that logs all DEBUG logs and an email log handler 
 that will only be used for CRITICAL logs. In this regard, the logger-handler relationship is similar to a 
 publisher-consumer one: A log will be broadcast to all handlers once it passes the logger level check.

Loggers have a hierarchy. On top of the hierarchy is the root logger, which can be accessed via logging.root.
This logger is called when methods like logging.debug() is used. By default, the root log level is WARN, so 
every log with lower level (for example via logging.info("info")) will be ignored. Another particularity of 
the root logger is that its default handler will be created the first time a log with a level greater than 
WARN is logged. Using the root logger directly or indirectly via methods like logging.debug() is generally 
not recommended.

By default, when a new logger is created, its parent will be set to the root logger:
lab = logging.getLogger("a.b")
assert lab.parent == logging.root       # lab's parent is indeed the root logger

However, the logger uses the “dot notation,” meaning that a logger with the name “a.b” will be the child of 
the logger “a.” However, this is only true if the logger “a” has been created, otherwise “ab” parent is still
 the root.

la = logging.getLogger("a")
assert lab.parent == la # lab's parent is now la instead of root

When a logger decides whether a log should pass according to the level check (e.g., if the log level is lower
than logger level, the log will be ignored), it uses its “effective level” instead of the actual level. The effective level
is the same as logger level if the level is not NOTSET, i.e., all the values from DEBUG up to CRITICAL; however, if the logger
level is NOTSET, then the effective level will be the first ancestor level that has a non-NOTSET level.

By default, a new logger has the NOTSET level, and as the root logger has a WARN level, the logger’s effective level will be
WARN. So even if a new logger has some handlers attached, these handlers will not be called unless the log level exceeds 
WARN:

mylogger = logging.getLogger("tst")
assert mylogger.level == logging.NOTSET               # new logger has NOTSET level
assert mylogger.getEffectiveLevel() == logging.WARN   # and its effective level is the root logger level, i.e. WARN

# Attach a console handler to toto_logger
console_handler = logging.StreamHandler()
mylogger.addHandler(console_handler)
mylogger.debug("debug")                 # nothing is displayed as the log level DEBUG is smaller than toto effective level
mylogger.setLevel(logging.DEBUG)
mylogger.debug("debug message")         # now you should see "debug message" on screen

By default, the logger level will be used to decide of the a log passes: If the log level is lower than logger level, 
the log will be ignored. But if the level of root is not at NOTSET level, then the greater level out of two(root and logger)
will decide which level logs have to be printed.

Steps:
Setting up logger:

logger = logging.getLogger("test")
logger.setLevel(level=logging.DEBUG)

Adding a stream handler
We’ll configure our stream handler to send the log to our console, printing it out:

logStreamFormatter = logging.Formatter(
  fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s", 
  datefmt="%H:%M:%S"
)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(logStreamFormatter)
consoleHandler.setLevel(level=logging.DEBUG)
logger.addHandler(consoleHandler)

Here sys.stdout is writing the output directly to screen console. 
Now when we use level=logging.DEBUG , so it will show all logs having level equal or greater than this 
log level. Thus all logs will get printed. But if we take logging.INFO then DEBUG logs will be ignored 
and thus will not be printed. Similarly, we can ignore the logs according to the loglevel set using setLevel.

Adding a file handler
The steps are exactly the same as with the stream handler. The differences are that we specify another 
format and a different level.


logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename='test.log')
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.INFO)

logger.addHandler(fileHandler)

In this case, it will check for the level set for root if the logger level is greater than this root level then 
logs are printed according to logger level set. Otherwise, it will print all the logs having level equal and above
the root logging level.

To filter any one level of logs from all logs we should make a class that has a filter function to filter that level of 
log.
e.g.
class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

And then we can call that class to filter one level of log like here we are filtering only INFO logs only

fileHandler.addFilter(MyFilter(logging.INFO))





