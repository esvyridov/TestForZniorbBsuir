import re

file = open('./test/1.txt','r')
output_file = open('./test/output.txt','a') #дозапись
questions_list = []
i = j  =0
file_text = file.read()

questions = re.findall('\d..+[:?]',file_text)
answers = re.findall('\n.\).+',file_text)
right_answers = re.findall('==ОТВЕТ:(?P<p>\w+)',file_text)

for question in questions:

    output_file.write(("\n{'question' : '" + question.replace('\n','') + "'," +
           "\n'answer1' : '" + answers[i].replace('\n', '') + "'," +
           "\n'answer2': '" + answers[i + 1].replace('\n', '') + "',"+
           "\n'answer3' : '" + answers[i + 2].replace('\n', '') + "',"+
           "\n'answer4' : '" + answers[i + 3].replace('\n', '') + "',"+
           "\n'right' : '" + right_answers[j] + "',},"))

    i += 4
    j += 1



