article_title = input()
article_content = input()
whole_think = {}
comments = []
text = input()
while text != "end of comments":
    comments.append(text)
    text = input()

whole_think[article_title] = {article_content: comments}

for key, value in whole_think.items():
    print("<h1>")
    print(f"    {key}")
    print("</h1>")
    for k, v in value.items():
        print("<article>")
        print(f"    {k}")
        print("</article>")
        for comment in v:
            print("<div>")
            print(f"    {comment}")
            print("</div>")

