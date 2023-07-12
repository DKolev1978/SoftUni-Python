from abc import ABC, abstractmethod


class PrimaryWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(PrimaryWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(PrimaryWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class MegaWorker(PrimaryWorker):
    @staticmethod
    def work():
        print("I am working mega hard!!!")


class GigaWorker(PrimaryWorker):
    @staticmethod
    def work():
        print("I am working GIGA hard!!!")


class LazyWorker(PrimaryWorker):
    def work(self):
        print("Uf, I dont want to work...")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, PrimaryWorker):
            return f"`worker` must be subclass of type {PrimaryWorker}"

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
mega_worker = MegaWorker()
giga_worker = GigaWorker()
lazy_worker = LazyWorker()

try:
    manager.set_worker(super_worker)
    manager.manage()

    manager.set_worker(mega_worker)
    manager.manage()

    manager.set_worker(giga_worker)
    manager.manage()

    manager.set_worker(lazy_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
