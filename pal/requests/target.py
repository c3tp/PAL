import pal.config.defaults as defaults


class SymlinkTargetSpec(object):
    def __init__(self, target, mount_point): 
        self.target = target
        self.bucket, self.key = self.__parse_key_bucket(target)
        self.mount_point = (defaults.MOUNT_POINT + self.bucket + "/"
                            if mount_point is None
                            else mount_point)
        self.filepath = self.__define_target_filepath(self.key,
                                                      self.mount_point)

    def __parse_key_bucket(self, target):
        return target.split('/', 1)
    
    def __define_target_filepath(self, key, mount_point):
        return mount_point + key