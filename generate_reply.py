reply_yes = "Either Scan the QR code or Pay using UPI ID:\n\n{}\n\nIt works for all " \
            "GPay/PhonePay/PayTM etc.\n\nAfter the payment is successful send your Email Address and Payment " \
            "Screenshot."

reply_start = "Hey {}!!\nThis is a download link for the sample material.\n\n" \
              "{}\n\nCost of complete course material=[Rs:{}].\n\nDo you want to buy?\n.\n."

reply_no = "If you pressed NO by mistake, Click /start to restart the process.\n\nIf this was intentional, " \
           "Thanks for your time."


def forward_message_to_admin(bot, user, message):
    bot.send_message("{}-{}-{}: {}".format(user.get("first_name"),
                                           user.get("username"),
                                           user.get("type"),
                                           message), bot.ADMIN_CHAT_ID)


def response(bot, input_text, photoid, from_, user):
    keypad_input = None
    if photoid:
        bot.send_image(bot.ADMIN_CHAT_ID, photoid)
        forward_message_to_admin(bot, user, "screenshot")
        reply = "Processing your request, it might take few minutes. Don't Panic. Keep checking your mail."
    else:
        if input_text == "/start":
            reply = reply_start.format(user.get("first_name"), bot.DEMO_MATERIAL_PUBLIC_LINK, bot.MATERIAL_COST)
            keypad_input = ["YES", "NO"]
        elif input_text == "YES":
            reply = reply_yes.format(bot.UPI_ID)
            bot.send_image_from_local(from_)
        elif input_text == "NO":
            reply = reply_no
            keypad_input = ["/start"]
        elif '@' in input_text:
            forward_message_to_admin(bot, user, input_text)
            reply = "Email-ID Received. Send Payment Screenshot"
            keypad_input = ["SENT"]
        elif input_text == "SENT":
            reply = "Processing your request, it might take few minutes. Don't Panic."
        else:
            reply = "Wrong Input, Try Again"
            keypad_input = ["/start"]
    return reply, keypad_input
