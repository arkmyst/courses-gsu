public class RunProcesses {

    public static void main(String[] args) {

        Process coffee = new Process("coffee");
        Process cookie = new Process("cookie");
        Process conversation = new Process("conversation");

        coffee.start();
        cookie.start();
        conversation.start();
    }
}
