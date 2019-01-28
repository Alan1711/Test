Question 2: Whats wrong with the given code below:

public class Main {

public static void main(String[] args) {

System.out.println(fixSpelling("hostleworld"));

}

public static String fixSpelling(String name) {

String wordToCheck = new String(name);

## '==' should be '==='

if(wordToCheck == "hostleworld" )

name = "hostelworld";

}

else {

fixSpelling(name);

}

return name;

}

}
