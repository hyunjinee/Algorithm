import java.io.*;
import java.util.*;

public class p2470 {
  static int n , start, n ;
  static int[] liquid;
  static int[] answer = new int[2];
  static int max = 2000000000;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    n = Integer.parseInt(br.readline())
    liquid = new int [n]
    st = new StringTokenizer(br.readLine())
for (int i = 0; i < n; i++) {
			liquid[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(liquid);
		// System.out.println(Arrays.toString(liquid));
		start = 0;
		end = n - 1;
		while (start != end) {
			int com = liquid[start] + liquid[end];
			// 만약 특성값이 더 작다면 갱신
			if (Math.abs(max) >= Math.abs(com)) {
				max = com;
				answer[0] = liquid[start];
				answer[1] = liquid[end];
			}
			// 여기서 특성값을 더 줄일 수 있게 포인터를 조정해야 함.
			// start를 움직이느냐, end를 움직이느냐 -> 절대값이 더 큰 녀석을 움직이자
			if (Math.abs(liquid[start]) > Math.abs(liquid[end])) {
				start += 1;
			} else {
				end -= 1;
			}


  }

  System.out.println(answer[0] + " " + answer[1]);
}