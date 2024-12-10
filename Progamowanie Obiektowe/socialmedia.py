class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        # print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(f"This is my username: {self.username}")
        postindicator = 1
        for i in range(0,len(self.posts)):
            print(f"{postindicator}. {self.posts[i]}")
            postindicator += 1
def main():
    
    user = SocialMediaProfile(username='jhondoe')
    user.add_post(content="Hello, world!")
    user.add_post(content="Had a gread day at the park!")
    user.add_post(content="What's up, Natalie? How are you?")

    user.display_timeline()

if __name__ == "__main__":
    main()
