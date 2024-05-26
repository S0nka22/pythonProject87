class Smartphone:
    def __init__(self, memory):
        """
        Initialize the smartphone with given memory.
        The smartphone is initially turned off and has no installed applications.

        :param memory: Total internal memory of the smartphone in MB
        """
        self.memory = memory
        self.available_memory = memory
        self.is_on = False
        self.installed_apps = {}

    def turn_on(self):
        """Turn the smartphone on."""
        if not self.is_on:
            self.is_on = True
            print("Smartphone is now ON.")
        else:
            print("Smartphone is already ON.")

    def turn_off(self):
        """Turn the smartphone off."""
        if self.is_on:
            self.is_on = False
            print("Smartphone is now OFF.")
        else:
            print("Smartphone is already OFF.")

    def install_app(self, app_name, app_size):
        """
        Install an application if there is enough available memory.

        :param app_name: Name of the application to install
        :param app_size: Memory required for the application in MB
        """
        if not self.is_on:
            print("Cannot install applications while the smartphone is OFF.")
            return

        if app_name in self.installed_apps:
            print(f"Application '{app_name}' is already installed.")
            return

        if app_size > self.available_memory:
            print(
                f"Not enough memory to install '{app_name}'. Required: {app_size} MB, Available: {self.available_memory} MB.")
        else:
            self.installed_apps[app_name] = app_size
            self.available_memory -= app_size
            print(
                f"Application '{app_name}' installed successfully. Used: {app_size} MB, Available: {self.available_memory} MB.")

    def uninstall_app(self, app_name):
        """
        Uninstall an application and free up its memory.

        :param app_name: Name of the application to uninstall
        """
        if not self.is_on:
            print("Cannot uninstall applications while the smartphone is OFF.")
            return

        if app_name in self.installed_apps:
            app_size = self.installed_apps.pop(app_name)
            self.available_memory += app_size
            print(
                f"Application '{app_name}' uninstalled successfully. Freed: {app_size} MB, Available: {self.available_memory} MB.")
        else:
            print(f"Application '{app_name}' is not installed.")


# Example usage
phone = Smartphone(1024)  # Smartphone with 1024 MB internal memory
phone.turn_on()
phone.install_app("WhatsApp", 100)
phone.install_app("Instagram", 200)
phone.uninstall_app("Canva")
phone.turn_off()
