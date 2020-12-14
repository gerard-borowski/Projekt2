from abc import ABCMeta, abstractmethod


class Client(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        raise NotImplementedError


class LinuxClient(Client):
    def connect(self):
        print("Linux client is connected")


class WindowsClient(Client):
    def connect(self):
        print("Windows client is connected")


class MacOSClient(Client):
    def connect(self):
        print("Mac OS client is connected")


class SolarisClient(Client):
    def connect(self):
        print("Solaris client is connected")


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ClientsFactory(metaclass=Singleton):
    _registered_clients = {
       "linux": LinuxClient,
       "windows": WindowsClient,
       "macos": MacOSClient
    }

    @property
    @classmethod
    def registered_clients(cls):
        return cls._registered_clients

    @classmethod
    def register_client(cls, platform: str, client: Client):
        if platform in cls._registered_clients:
            raise Exception(f"Platform {platform} is already registered")
        cls._registered_clients[platform] = client

    @classmethod
    def create_client(cls, platform: str) -> Client:
        if platform not in cls._registered_clients:
            raise Exception(f"Platform {platform} is not registered")
        client_cls = cls._registered_clients[platform]
        return client_cls()


ClientsFactory.register_client("solaris", SolarisClient)


if __name__ == "__main__":
    client = ClientsFactory.create_client("solaris")
    client.connect()
