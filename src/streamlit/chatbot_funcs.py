def response_generator():
    import random
    import time

    response = random.choice(
        [
            "Olá! Como posso ajudar você hoje?",
            "Oi, humano! Existe alguma coisa com a qual eu possa te ajudar?",
            "Você precisa de ajuda?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
