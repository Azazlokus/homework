class NewThread implements Runnable{
    Thread t;
    int id;
    private static int currentId = 1;
    private final static Object lock = new Object();

    NewThread(String name, int id){
        this.id = id;
        t = new Thread(this, name);
        System.out.println("Thread start: " + t.getName());
        t.start();
    }

    public void run(){
        while(true) {
            try {
                synchronized(lock){
                    while(this.id != currentId){
                        lock.wait();  
                    }
                    System.out.println(Thread.currentThread().getName());
                    currentId = (currentId == 1) ? 2 : 1;
                    Thread.sleep(1000);
                    lock.notify();
                }
            } 
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class ThreadDemo{
    public static void main(String[] args) {
        new NewThread("Thread1", 1);
        new NewThread("Thread2", 2);
    }
}
