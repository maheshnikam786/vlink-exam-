
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n=0;
		Scanner sc= new Scanner(System.in);
		n=sc.nextInt();
		
		
		if(n<=0){
			System.out.println("Invalid input");
		}else{
			ArrayList<String> AL=new ArrayList<String>();
			for(int i=0;i<=n;i++){
			AL.add(sc.next());
			}
				
		int min = AL.get(0).length();
		String res=AL.get(0);
		for( int i=1;i<AL.size();i++){
			if(min>AL.get(i).length()){
				min=AL.get(i).length();
				res=AL.get(i);
			}
		}
		System.out.println(res);
		}
	}
}

