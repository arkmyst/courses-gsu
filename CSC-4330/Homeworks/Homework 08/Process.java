import java.util.Random;

public class Process implements Runnable {

    private Thread t;
    private String name;
    private Random r = new Random();

    public Process(String name) {
        this.name = name;
        System.out.println("creating " + name);
    }

    public void start() {
        System.out.println("starting " + name);
        t = new Thread(this, name);
        t.start();
    }

    public void run() {
        System.out.println("running " + name);

        try {
            // random pause before starting
            Thread.sleep(r.nextInt(1000));
        } catch (InterruptedException e) {}

        // behavior depends on process type
        if (name.equals("coffee")) {
            System.out.println("drink coffee");
        }
        else if (name.equals("cookie")) {
            System.out.println("eat cookie");
        }
        else if (name.equals("conversation")) {
            System.out.println("think");

            try {
                Thread.sleep(r.nextInt(1000));
            } catch (InterruptedException e) {}

            System.out.println("talk");
        }

        System.out.println("thread " + name + " exiting");
    }
}
