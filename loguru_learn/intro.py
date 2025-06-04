from loguru import logger
import sys

# # 定义统一的日志格式字符串
# log_format = '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <yellow>{level:<8}</yellow> | {module}:{function}:{line} - {message}'
#
# logger.remove()
# logger.add(sys.stdout, format=log_format, level="INFO", colorize=True)
# logger.info("That's it, beautiful and simple logging!")


# logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")


# 3. Fully descriptive exceptions
# Logging exceptions that occur in your code is important to track bugs, but it’s quite useless if you don’t know why it failed. Loguru helps you identify problems by allowing the entire stack trace to be displayed, including values of variables (thanks better_exceptions for this!).
# https://github.com/Qix-/better-exceptions
# Caution, "diagnose=True" is the default and may leak sensitive data in prod
logger.add("out.log", backtrace=False, diagnose=True)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)