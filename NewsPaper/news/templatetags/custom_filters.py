from django import template


register = template.Library()

@register.filter()
def censor(value):
    new_string = []
    badword_list = ['жопа', 'вареники', 'промышленность', 'сыр', 'ученый', 'коронавирус']
    splited_text = value.split(' ')
    for word in splited_text:
        if word in badword_list:
            new_string.append(word[0]+(len(word)-1)*'*')
        else:
            new_string.append(word)
    value = ' '.join(new_string)
    return value
