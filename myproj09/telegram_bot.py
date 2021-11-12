import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요.", file=sys.stderr)
    sys.exit(1)  # 종료 상탯값을 1로 지정하고, 프로그램 종료

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕. 나는 raspberrypybot이야. 만나서 반가워.")


def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [tasks. ya,
                       tasks.naver_search,
                       tasks. self,
                       tasks.ins,
                       tasks.pyy,
                       tasks.reverse_string,
                       tasks.predict_lotto_numbers,
                       tasks.get_current_lotto_numbers,
                       ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
        else :
            response_text = "지원하지 않는 명령입니다."

    # if tasks.ya.check_available(received_text):
    #     response_text = tasks.ya.make_response(received_text)
    # elif tasks.naver_search.check_available(received_text):
    #     response_text = tasks.naver_search.make_response(received_text)
    # elif tasks.pyy.check_available(received_text):
    #     response_text= tasks.pyy.make_response(received_text)
    # elif tasks.ins.check_available(received_text):
    #     response_text=tasks.ins.make_response(received_text)
    # elif tasks.self.check_available(received_text):
    #     response_text=tasks.self.make_response(received_text)
    # else:
    #     response_text = "지원하지 않는 명령입니다."

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

print("started bot...")

updater.start_polling()
updater.idle()


