class Solution {
 List<String> addOperators(String num, int target) {
  List<String> result = [];
  helper(result, "", num, target, 0, 0, 0);
  return result;
}

void helper(List<String> result, String path, String num, int target, int pos, int eval, int multed) {
  if (pos == num.length) {
    if (eval == target) {
      result.add(path);
    }
    return;
  }

  for (int i = pos; i < num.length; i++) {
    if (i != pos && num[pos] == '0') {
      break;
    }

    int cur = int.parse(num.substring(pos, i + 1));
    if (pos == 0) {
      helper(result, cur.toString(), num, target, i + 1, cur, cur);
    } else {
      helper(result, "$path+$cur", num, target, i + 1, eval + cur, cur);
      helper(result, "$path-$cur", num, target, i + 1, eval - cur, -cur);
      helper(result, "$path*$cur", num, target, i + 1, eval - multed + multed * cur, multed * cur);
    }
  }
}

}