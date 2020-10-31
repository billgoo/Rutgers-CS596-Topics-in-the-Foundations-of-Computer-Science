clear;
cla;
cla reset;
m = load('hw4-2data.mat');

% c = circle, s = stars
s = m.stars;
c = m.circles;

% plot the point
scatter(s(:,1) ,s(:,2), 'red','+');
hold on;
scatter(c(:,1),c(:,2),'blue','d');
hold on; 

[szs, szs_] = size(s);
[szc, szc_] = size(c);
sz = szc + szs

K = zeros(sz, sz);
points = vertcat(s, c);
h = [0.01, 0.1, 1, 10];
lambda = [0.01, 0.1, 1, 10];

for hi = 1:4
    for lambdai = 1:4
        % plot the point
        scatter(s(:,1) ,s(:,2), 'red','+');
        hold on;
        scatter(c(:,1),c(:,2),'blue','d');
        hold on; 
        
        % First, calculate the kernel function, it is the 42*42 matrix.
        for i = 1:sz
            for j = 1:sz
                 K(i,j) = exp(-1 / h(hi) * ((points(i,1) - points(j,1)) ^ 2 + (points(i,2) - points(j,2)) ^ 2));
            end
        end

        % calculate gamma,b
        % gamma = [a1, a2, a3, ..., ai, b1, b2, ..., bi]
        % b for update
        Gamma = zeros(sz,sz);
        b = zeros(sz,1);

        % stars
        for i=1:sz/2
            b = b + K(:,i);
            Gamma = Gamma + K(:,i) * K(i,:); 
        end
        % circles
        for i=sz/2+1:sz
            b = b - K(:,i);
            Gamma = Gamma + K(:,i) * K(i,:) ; 
        end

        Gamma = Gamma + lambda(lambdai) * K;
        res = Gamma \ b;
        Gamma = res;

        m = linspace(-1, 1, 100);
        n = zeros(100);
        syms m n
        L = 0;
        for i=1:sz
            L = L + Gamma(i) * exp(-((m - points(i,1)) ^ 2 + (n - points(i,2)) ^ 2) / h(hi));
        end
        
        % show alpha and beta
        Gamma
        
        line = fimplicit(L, [-1.25, 1.25]);
        line.Color = 'black';
        title(['h = ',num2str(h(hi)), ', {\lambda} = ', num2str(lambda(lambdai))]);
        % clear scatter;
    end
end

