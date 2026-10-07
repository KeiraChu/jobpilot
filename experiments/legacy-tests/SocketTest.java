package com.job;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.*;
import java.net.Socket;

@SpringBootTest
public class SocketTest {
    //@Test
    public void testSocket() {
        try {
            String ip = "192.168.171.211";
            int port = 50007;
            Socket client = new Socket(ip, port);
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

    //@Test
    void test1() throws IOException {
        // 创建Socket客户端
        Socket socket = new Socket("localhost", 12345);
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

    //@Test
    void testCallModel() {
        String IP = "localhost";
        int PORT = 12345;
        Socket socket = null;
        String result = null;
        String filePath = "./model/resumes/resume.xlsx";

        try {
            socket = new Socket(IP, PORT);
            //socket.setSoTimeout(10000); //单位为毫秒
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println(filePath);

            System.out.println("准备接收消息...");
            System.out.println("服务器返回的信息: ");

            // 接受消息方法一
            InputStreamReader inputStreamReader = new InputStreamReader(socket.getInputStream(), "utf-8");
            BufferedReader in = new BufferedReader(inputStreamReader);
            result = in.readLine();
            System.out.println(result);

            System.out.println("接收回复信息完成");

            // 接收消息方法二，有bug
            /*InputStream inputStream = socket.getInputStream();
            byte[] buf = new byte[1024];
            StringBuilder msg = new StringBuilder();
            for (int len = inputStream.read(buf); len > 0; len = inputStream.read(buf)) {
                msg.append(new String(buf, 0, len));
            }
            System.out.println(msg);*/
            /*String tmp;
            StringBuilder stringBuilder = new StringBuilder();
            // 读取内容
            while ((tmp=in.readLine()) != null) {
                stringBuilder.append(tmp).append("\n");
            }
            System.out.println("Response: " + stringBuilder);*/

            /*InputStream inputStream = socket.getInputStream();
            Scanner scanner = new Scanner(inputStream, "utf-8");
            while (scanner.hasNextLine()) {
                System.out.println(444);
                stringBuilder.append(scanner.nextLine());
                System.out.println(555);
                System.out.println(stringBuilder);
            }*/
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (socket != null) {
                    socket.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
