package com.example;
public class UserService {
    private UserDao userDao;
    private UserRepository userRepository;

    public UserService(UserDao userDao) { this.userDao = userDao; }
    public UserService(UserRepository userRepository) { this.userRepository = userRepository; }

    public User getUserById(int id) { return userDao.getUserById(id); }
    public void addUser(User user) { userRepository.save(user); }
}
