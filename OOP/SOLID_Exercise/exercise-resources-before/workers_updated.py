from abc import ABC, abstractmethod
import time


class Workable(ABC):
    @abstractmethod
    def work(self):
        ...


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        ...


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class MegaWorker(Workable, Eatable):
    def work(self):
        print("I'm mega worker. I work mega hard!")

    def eat(self):
        print("Lunch break....(2 secs)")
        time.sleep(3)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class LazyWorker(Workable, Eatable):
    def work(self):
        print("I'm lazy worker. I work as I am working in Bulgarian Parliament!")

    def eat(self):
        print("Lunch break....(12 hours)")
        time.sleep(3)


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


class GigaRobotWorker(Workable):
    def work(self):
        print("I'm a giga robot. I'm working....giga hard")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        if not isinstance(worker, Eatable):
            return f"`worker` must be of type {Eatable}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()

worker = Worker()
work_manager.set_worker(worker)
break_manager.set_worker(worker)
work_manager.manage()
break_manager.lunch_break()

super_worker = SuperWorker()
work_manager.set_worker(super_worker)
break_manager.set_worker(super_worker)
work_manager.manage()
break_manager.lunch_break()

mega_worker = MegaWorker()
work_manager.set_worker(mega_worker)
break_manager.set_worker(mega_worker)
work_manager.manage()
break_manager.lunch_break()

lazy_worker = LazyWorker()
work_manager.set_worker(lazy_worker)
break_manager.set_worker(lazy_worker)
work_manager.manage()
break_manager.lunch_break()

giga_robot_worker = GigaRobotWorker()
work_manager.set_worker(giga_robot_worker)
break_manager.set_worker(giga_robot_worker)
work_manager.manage()
break_manager.lunch_break()

robot = Robot()
work_manager.set_worker(robot)
work_manager.manage()
break_manager.set_worker(robot)
