from database import Thread

threads = Thread.select()
print(threads[0].name)
print(threads[11].name)

threads = Thread.select().where(Thread.name == "keisuke01").get()
print(threads.name, threads.title, threads.body)
