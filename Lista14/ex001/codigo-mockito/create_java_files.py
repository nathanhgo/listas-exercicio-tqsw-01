import os

base_src_dir = r"C:\Users\ideapad3\.gemini\antigravity\scratch\mockito-tutorial\src\main\java\com\example"
base_test_dir = r"C:\Users\ideapad3\.gemini\antigravity\scratch\mockito-tutorial\src\test\java\com\example"

os.makedirs(base_src_dir, exist_ok=True)
os.makedirs(base_test_dir, exist_ok=True)

src_files = {
    "ExampleService.java": """package com.example;
public class ExampleService {
    public String exampleMethod() { return "Real"; }
}
""",
    "User.java": """package com.example;
public class User {
    private int id;
    private String username;
    private String email;
    private String firstName;
    private String lastName;

    public User() {}
    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public void setId(int id) { this.id = id; }
    public void setUsername(String username) { this.username = username; }
    public void setEmail(String email) { this.email = email; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        User user = (User) obj;
        return id == user.id && 
               (username != null ? username.equals(user.username) : user.username == null) &&
               (email != null ? email.equals(user.email) : user.email == null);
    }
}
""",
    "UserDao.java": """package com.example;
public class UserDao {
    public User getUserById(int id) { return null; }
}
""",
    "UserService.java": """package com.example;
public class UserService {
    private UserDao userDao;
    private UserRepository userRepository;

    public UserService(UserDao userDao) { this.userDao = userDao; }
    public UserService(UserRepository userRepository) { this.userRepository = userRepository; }

    public User getUserById(int id) { return userDao.getUserById(id); }
    public void addUser(User user) { userRepository.save(user); }
}
""",
    "UserRepository.java": """package com.example;
public class UserRepository {
    public void save(User user) {}
}
""",
    "Calculator.java": """package com.example;
public class Calculator {
    public int divide(int a, int b) { return a / b; }
}
""",
    "MyDependency.java": """package com.example;
public class MyDependency {
    public String getDependencyValue() { return "RealDependency"; }
}
""",
    "MyClass.java": """package com.example;
public class MyClass {
    private MyDependency dependency;

    public MyClass() {}
    public MyClass(MyDependency dependency) { this.dependency = dependency; }

    public String publicMethod() { return privateMethod(); }
    private String privateMethod() { return "RealPrivate"; }

    public static String staticMethod(String input) { return "RealStatic"; }
    public String getDependencyValue() { return dependency.getDependencyValue(); }
}
""",
    "UserUtils.java": """package com.example;
public class UserUtils {
    public static String generateUserName(String name) { return name.toLowerCase().replace(" ", ""); }
}
"""
}

test_files = {
    "ExampleTest.java": """package com.example;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.List;
import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

public class ExampleTest {

    @Mock
    private ExampleService exampleService;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
    }

    @After
    public void tearDown() {
        reset(exampleService);
    }

    @Test
    public void testMockObjectAndStubbing() {
        Example example = mock(Example.class);
        when(example.doSomething()).thenReturn("Hello");
        assertEquals("Hello", example.doSomething());
    }

    @Test
    public void testMethodCallVerification() {
        List<String> mockedList = mock(List.class);
        mockedList.add("a");
        mockedList.add("b");
        mockedList.add("c");
        mockedList.add("c");

        verify(mockedList).add("a");
        verify(mockedList).add("b");
        verify(mockedList, times(2)).add("c");
        verify(mockedList, times(4)).add(anyString());
        verify(mockedList, never()).clear();
    }

    @Test
    public void testMethodBehavior() {
        List<String> mockedList = mock(List.class);
        mockedList.add("a");
        verify(mockedList).add("a");
    }

    @Test
    public void testExampleMethod() {
        when(exampleService.exampleMethod()).thenReturn("Hello, World!");
        String result = exampleService.exampleMethod();
        verify(exampleService).exampleMethod();
        assertEquals("Hello, World!", result);
    }
}
""",
    "UserServiceTest.java": """package com.example;
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
""",
    "CalculatorTest.java": """package com.example;
import org.junit.Test;
import org.mockito.Mockito;
import static org.junit.Assert.assertThrows;

public class CalculatorTest {

    @Test
    public void testDivideByZero() {
       Calculator calculator = Mockito.mock(Calculator.class);
       
       Mockito.when(calculator.divide(Mockito.anyInt(), Mockito.eq(0)))
              .thenThrow(new ArithmeticException("Division by zero"));
       
       assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));
    }
}
""",
    "MyClassTest.java": """package com.example;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;
import static org.junit.Assert.assertEquals;

@RunWith(PowerMockRunner.class)
@PrepareForTest({MyClass.class, UserUtils.class})
public class MyClassTest {

   @Test
   public void testPrivateMethod() throws Exception {
      MyClass myClass = new MyClass();
      
      MyClass spyClass = PowerMockito.spy(myClass);
      PowerMockito.doReturn("mockedValue").when(spyClass, "privateMethod");
      
      String result = spyClass.publicMethod();
      
      assertEquals("mockedValue", result);
   }

   @Test
   public void testStaticMethod() {
      PowerMockito.mockStatic(MyClass.class);
      Mockito.when(MyClass.staticMethod(Mockito.anyString()))
             .thenReturn("mockedValue");
             
      String result = MyClass.staticMethod("input");
      
      assertEquals("mockedValue", result);
   }

   @Test
   public void testConstructor() {
      MyDependency myDependencyMock = Mockito.mock(MyDependency.class);
      Mockito.when(myDependencyMock.getDependencyValue())
             .thenReturn("mockedValue");
             
      MyClass myClass = new MyClass(myDependencyMock);
      
      assertEquals("mockedValue", myClass.getDependencyValue());
   }

   @Test
   public void testUserUtilsStaticMethod() {
       PowerMockito.mockStatic(UserUtils.class);
       Mockito.when(UserUtils.generateUserName(Mockito.anyString())).thenReturn("johndoe");
       
       String userName = UserUtils.generateUserName("John Doe");
       assertEquals("johndoe", userName);
       
       PowerMockito.verifyStatic(UserUtils.class);
       UserUtils.generateUserName(Mockito.anyString());
   }
}
"""
}

for filename, content in src_files.items():
    with open(os.path.join(base_src_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

for filename, content in test_files.items():
    with open(os.path.join(base_test_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

print("Java files created successfully!")
