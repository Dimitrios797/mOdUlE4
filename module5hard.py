import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # in seconds
        self.time_now = 0  # current playback time
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title} ({self.duration}s)"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Invalid credentials")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Automatically log in after registration

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        return [video.title for video in self.videos if search_term.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    print(video.time_now + 1)
                    time.sleep(1)  # Simulate watching the video
                    video.time_now += 1

                print("Конец видео")
                video.time_now = 0  # Reset playback time
                return

        print("Видео не найдено")


# Testing the implementation
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Adding videos
ur.add(v1, v2)

# Checking search functionality
print(ur.get_videos('лучший'))  # Expected: ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # Expected: ['Лучший язык программирования 2024 года']

# Checking user login and age restriction
ur.watch_video('Для чего девушкам парень программист?')  # Expected: "Войдите в аккаунт, чтобы смотреть видео"
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Registering a user underage
ur.watch_video('Для чего девушкам парень программист?')  # Expected: "Вам нет 18 лет, пожалуйста покиньте страницу"
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Registering an adult user
ur.watch_video('Для чего девушкам парень программист?')  # Expected: Playback of the video

# Checking login for existing account
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Attempt to register existing user
print(ur.current_user)  # Expected: urban_pythonist

# Attempting to play a non-existing video
ur.watch_video('Лучший язык программирования 2024 года!')  # Expected: "Видео не найдено"