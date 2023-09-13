---
title: "VRPSTW"
output:
    word_document:
        path: VRPSTW.docx
        toc: true
        toc_depth: 6
        number_sections: true
---
$$
\begin{aligned}
&参数\\
&C_{ij} -i到j的行驶成本\\
&t_{ij} -i到j的行驶时间\\
&C_1 -早到单位时间成本\\
&C_2 -晚到单位时间成本\\
&C_3 -派遣成本\\
&e_i -i点的开始时间窗\\
&l_i -i点的截止时间窗\\
&w_i -i点的服务时间\\
&q_i -i点的需求量\\
&Q_k -k车的承载上限\\
&0 -车场\\
&C -客户点集合\\
&N -0\cup C\\
&K -车辆集合\\
&M -极大值\\
&决策变量\\
&x_{ijk} -k车从i行驶到j时为1，否则为0\\
&t^0_{ik} -k车到达i点的时间\\
&t^1_{ik} -k车离开i点的时间\\
&q_{ik} -k车在i点的累计载重量\\
\end{aligned}
$$
$$
\begin{aligned}
&参数\\
&min　z=行驶成本+早到成本+晚到成本+派遣成本\\
&行驶成本=\sum_{i\in N}\sum_{j\in N}\sum_{k\in K}c_{ij}x_{ijk}\\
&早到成本=C_1\sum_{i\in C}\sum_{k\in K}max\{e_i-t^0_{ik},0\}\\
&晚到成本=C_2\sum_{i\in C}\sum_{k\in K}max\{t^0_{ik}-l_i,0\}\\
&派遣成本=C_3\sum_{i\in C}\sum_{k\in K}x_{oik}\\
&\sum_{j\in N\setminus \{i\}}\sum_{k\in K}x_{ijk}=1,\forall i\in C\\
&\sum_{i\in C}\sum_{k\in K}x_{oik}\leq 1\\
&\sum_{j\in N\setminus \{i\}}x_{ijk}=\sum_{j\in N\setminus \{i\}}x_{jik},\forall i\in N,k\in K\\
&t^1_{ik}\geq e_i+w_i,\forall i\in C,\forall k\in K\\
&t^1_{ik}\geq t^0_{ik}+w_i,\forall i\in C,\forall k\in K\\
&t^0_{jk}+M(1-x_{ijk})\geq t^1_{ik}+t_{ij},\forall i,j\in N,k\in K,i\neq j\\
&q_{jk}+M(1-x_{ijk})\geq q_{ik}+q_i,\forall i\in C,j\in N,k\in K,i\neq j\\
&t^0_{ik}\geq 0,t^1_{ik}\geq 0,0\leq q_{ik}\leq Q_k,\forall i\in N,k\in K\\
&x_{ijk}=\{0,1\},\forall i,j\in N,k\in K\\
\end{aligned}
$$