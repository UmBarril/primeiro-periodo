public class Sysout extends Object {
    public static void main(String[] args) {
        printf("SAUDAÇÕES: %s %s %s", "Olá", "você é", "muito legal");
    }

    public static void printf(String format, String ... replacements) {
        String finalString = format;
        for(String r : replacements) {
            finalString = finalString.replaceFirst("%s", r);
        }
        System.out.print(finalString);
    }

}