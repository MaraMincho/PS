
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.IntStream;

class Solution {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("aaa");
        list.add("bbb");
        list.add("ccc");

        list.sort((Comparator<String>) (str1, str2) -> str1.compareTo(str2));
        Collections.reverse(list);
        System.err.println(list); 
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> cur = IntStream.of(nums1).map($0 -> $0.object);
    }
}
