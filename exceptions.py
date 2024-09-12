public class ArithmeticExceptionExample {
    public static void main(String[] args) {
        int result = 10 / 0; // This will cause ArithmeticException
        System.out.println(result);
    }
}


public class ArithmeticExceptionHandling {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // This will cause ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception caught: " + e.getMessage());
        }
    }
}


public class ExceptionThrowingMethod {
    public static void throwException() throws ArithmeticException {
        throw new ArithmeticException("Exception thrown from method");
    }

    public static void main(String[] args) {
        throwException(); // No try block here
    }
}



public class MultipleCatchBlocks {
    public static void main(String[] args) {
        try {
            int[] array = new int[5];
            array[10] = 30 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception caught: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index Out Of Bounds Exception caught: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("General Exception caught: " + e.getMessage());
        }
    }
}





public class CustomMessageException {
    public static void main(String[] args) {
        try {
            throw new Exception("This is a custom exception message");
        } catch (Exception e) {
            System.out.println("Caught Exception: " + e.getMessage());
        }
    }
}




class MyCustomException extends Exception {
    public MyCustomException(String message) {
        super(message);
    }
}

public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            throw new MyCustomException("This is my custom exception");
        } catch (MyCustomException e) {
            System.out.println("Caught MyCustomException: " + e.getMessage());
        }
    }
}







public class FinallyBlockExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // This will cause ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught Arithmetic Exception: " + e.getMessage());
        } finally {
            System.out.println("This is the finally block, always executed");
        }
    }
}





public class GenerateArithmeticException {
    public static void main(String[] args) {
        // This line will cause an ArithmeticException (division by zero)
        int result = 10 / 0; 
        
        // This line won't be executed due to the exception above
        System.out.println("Result: " + result);
    }
}







import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;

public class FileNotFoundExceptionExample {
    public static void main(String[] args) {
        try {
            File file = new File("nonexistentfile.txt");
            FileReader fr = new FileReader(file);
        } catch (FileNotFoundException e) {
            System.out.println("FileNotFoundException caught: " + e.getMessage());
        }
    }
}



public class ClassNotFoundExceptionExample {
    public static void main(String[] args) {
        try {
            Class.forName("NonExistentClass");
        } catch (ClassNotFoundException e) {
            System.out.println("ClassNotFoundException caught: " + e.getMessage());
        }
    }
}




import java.io.FileReader;
import java.io.IOException;

public class IOExceptionExample {
    public static void main(String[] args) {
        try {
            FileReader reader = new FileReader("nonexistentfile.txt");
            reader.read();
        } catch (IOException e) {
            System.out.println("IOException caught: " + e.getMessage());
        }
    }
}



import java.lang.reflect.Field;

public class NoSuchFieldExceptionExample {
    public static void main(String[] args) {
        try {
            Class<?> c = Class.forName("java.lang.String");
            Field f = c.getField("nonExistentField");
        } catch (NoSuchFieldException e) {
            System.out.println("NoSuchFieldException caught: " + e.getMessage());
        } catch (ClassNotFoundException e) {
            System.out.println("ClassNotFoundException caught: " + e.getMessage());
        }
    }
}


