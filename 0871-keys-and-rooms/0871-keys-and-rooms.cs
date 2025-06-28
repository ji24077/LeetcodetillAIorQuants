public class Solution {
    public bool CanVisitAllRooms(IList<IList<int>> rooms) {
      int n = rooms.Count;
      bool[] visted = new bool[n];
      int vistedCount = 0;
      //this will change vistedCount, 
      void Room_DFS(int room){
        if(visted[room]){
          return;
        }
        visted[room] = true;
        vistedCount++;
        foreach(int key in rooms[room]){
          //rooms has room number that can go to other room
          Room_DFS(key);
        }


      }
      Room_DFS(0);
      return vistedCount == n;

    }
}