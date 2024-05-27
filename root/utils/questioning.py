def ask_the_bot(query, bot):
    response = bot.invoke(query)

    return response['result']