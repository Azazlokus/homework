javac .\#1\model\*.java
javac -cp ".\#1" .\#1\server.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#1;.\#1\model" .\#1\controller.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#1;.\#1\model" .\#1\Main.java