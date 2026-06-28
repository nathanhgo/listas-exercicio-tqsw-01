package com.example;
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
