javac .\#4\model\*.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#4;.\#4\model" .\#4\controller.java
javac --module-path .\Libs\javafx\lib --add-modules=javafx.controls,javafx.fxml --class-path ".\#4;.\#4\model" .\#4\Main.java