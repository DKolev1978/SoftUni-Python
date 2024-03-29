from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if new_name == self.name:
            return "Name cannot be the same."

        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    # def edit_comment(self, comment_number: int, new_comment: str):
    #     if comment_number > len(self.comments):
    #         return "Cannot find comment."
    #
    #     self.comments[comment_number] = new_comment
    #     return ", ".join(com for com in self.comments)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        else:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

