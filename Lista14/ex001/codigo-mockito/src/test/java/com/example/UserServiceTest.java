package com.example;
import org.junit.Test;
import org.mockito.Mockito;
import static org.junit.Assert.assertEquals;
import org.mockito.ArgumentCaptor;

public class UserServiceTest {

    @Test
    public void testGetUserById() {
       UserDao userDao = Mockito.mock(UserDao.class);
       
       User expectedUser = new User();
       expectedUser.setId(123);
       expectedUser.setUsername("testUser");
       expectedUser.setEmail("testUser@example.com");
       
       Mockito.when(userDao.getUserById(123)).thenReturn(expectedUser);
       
       UserService userService = new UserService(userDao);
       User actualUser = userService.getUserById(123);
       
       Mockito.verify(userDao).getUserById(123);
       assertEquals(expectedUser, actualUser);
    }

    @Test
    public void testAddUserArgumentCaptor() {
        UserRepository userRepository = Mockito.mock(UserRepository.class);
        UserService userService = new UserService(userRepository);
        
        ArgumentCaptor<User> captor = ArgumentCaptor.forClass(User.class);
        userService.addUser(new User("John", "Doe"));
        Mockito.verify(userRepository).save(captor.capture());
        
        User user = captor.getValue();
        assertEquals("John", user.getFirstName());
        assertEquals("Doe", user.getLastName());
    }

    @Test
    public void testAddUserSpy() {
        UserRepository userRepository = Mockito.spy(new UserRepository());
        UserService userService = new UserService(userRepository);
        userService.addUser(new User("John", "Doe"));
        Mockito.verify(userRepository).save(Mockito.any(User.class));
    }
}
