def update(btn1, btn2):
    return f'button 1: {btn1} & button 2: {btn2}'

def display(btn1, btn2, btn3, ctx):
    #print(ctx)
    #print(type(ctx))
    button_clicked = ctx.triggered_id
    return f'You last clicked button with ID {button_clicked}'