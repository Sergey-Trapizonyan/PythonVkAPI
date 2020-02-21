class VkUsers:
    def __init__(self, user_id, first_name, screen_name, is_banned):
        self.is_banned = is_banned
        self.first_name = first_name
        self.screen_name = screen_name
        self.id = user_id
