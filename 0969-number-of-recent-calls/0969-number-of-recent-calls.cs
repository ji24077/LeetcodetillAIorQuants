public class RecentCounter{
  //just count the most recent 3000ms and remove the old ms, keep the new ms.
  private Queue<int> requests;

  public RecentCounter(){
    requests = new Queue<int>();
    
  }
  public int Ping(int t)
  {
    requests.Enqueue(t); //u put the current time t into queue.

    while ( requests.Peek() < t - 3000){
      requests.Dequeue();
    }
    return requests.Count;
    

  }
}