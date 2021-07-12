//最大和問題
dp[i+1]=max(dp[i],dp[i]+a[i])//遷移式
//ナップサックDP
    /* n個の品物があり、i番目の品物のそれぞれ重さと価値が 
    weight[i],value[i] となっている (i=0,1,...,n−1i=0,1,...,n−1) 
    dp[i]dp[i] に対して、「今重さがどうなっているか」という情報が必要
    dp[i+1][w] := i番目までの品物の中から重さが ww を超えないように選んだときの、価値の総和の最大値
    dp[i+1][w]dp[i+1][w] の値を求めるには、以下のうち大きい方をとる:
        ・品物 (weight[i],value[i])を選ぶ場合 (w≥weight[i]の場合のみ)
            dp[i+1][w]　=　dp[i][w　−　weight[i]]　+　value[i]

        ･品物 (weight[i],value[i])を選ばない場合
            dp[i+1][w]=dp[i][w]
            
    <DP漸化式>    
        dp[i+1][w]= max(dp[i][w−weight[i]]+value[i],dp[i][w])　(w≥weight[i])　
                    dp[i][w]　　　　　　　　　　　　　　　　　　　(w<weight[i])
    <初期条件>
        dp[0][w]=0　(w=0,1,…,W)
    */
