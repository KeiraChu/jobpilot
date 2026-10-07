package com.job;

import org.springframework.boot.test.context.SpringBootTest;

import java.io.*;
import java.net.Socket;

@SpringBootTest
public class ModelTest {
    private String IP = "localhost";
    private int PORT = 12345;

    // csdn写法一
    public void callModel1(String filePath) {
        try {
            Socket client = new Socket(IP, PORT);
            OutputStreamWriter os = new OutputStreamWriter(client.getOutputStream());
            StringBuilder sb = new StringBuilder();
            sb.append("baidu.com").append("\r\n");
            os.write(sb.toString());
            os.flush();

            InputStream is = client.getInputStream();
            byte[] buf = new byte[1024 * 8];
            StringBuilder msg = new StringBuilder();
            for (int len = is.read(buf); len > 0; len = is.read(buf)) {
                msg.append(new String(buf, 0, len));
            }
            client.shutdownInput();
            System.out.println("正在接收回复信息...");
            System.out.println("服务器返回的信息: " + msg);
            System.out.println("接收回复信息完成");
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    // csdn写法二
    public void callModel2(String filePath) throws IOException {
        // 创建Socket客户端
        Socket socket = new Socket(IP, PORT);

        // 设置超时时间
        socket.setSoTimeout(10000); //单位为毫秒

        // 发送数据
        String inputData = "{\"features\": [1, 2, 3]}";
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        out.println(inputData);

        // 接收预测结果
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        String response = in.readLine();
        System.out.println("Prediction: " + response);

        // 关闭连接
        socket.close();
    }
}
