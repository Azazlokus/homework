javac -cp ".\#2" .\#2\ClientHandler.java
javac -cp ".\#2" .\#2\Server.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#2" .\#2\client.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#2" .\#2\Main.java