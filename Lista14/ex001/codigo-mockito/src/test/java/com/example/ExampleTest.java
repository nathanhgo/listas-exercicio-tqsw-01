package com.example;
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
