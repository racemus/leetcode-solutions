<?php

    class Solution {
    
    /**
     * @param TreeNode $root
     * @return Integer[][]
     */
    function verticalTraversal($root) {
        if ($root == null) {
            return [];
        }
        $queue = [[$root, 0]];
        $columns = [];
        while (!empty($queue)) {
            $size = count($queue);
            $cols = [];
            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);
                $cols[] = [$node[0]->val, $node[1]];
                if ($node[0]->left != null) {
                    $queue[] = [$node[0]->left, $node[1] - 1];
                }
                if ($node[0]->right != null) {
                    $queue[] = [$node[0]->right, $node[1] + 1];
                }
            }
            usort($cols, function($a, $b) {
                if ($a[1] == $b[1]) {
                    return $a[0] <=> $b[0];
                }
                return $a[1] <=> $b[1];
            });
            foreach ($cols as $col) {
                $columns[$col[1]][] = $col[0];
            }
        }
        ksort($columns);
        return array_values($columns);
    }
}


?>