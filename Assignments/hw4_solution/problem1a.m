r = rand(1000, 1);
x = [-2:0.004:1.996];
h = 1;
while h > 1e-6
    y = [];
    for i = 1:1000
        temp = 0;
        for j = 1:1000
            temp = temp + 1 / sqrt(2 * pi * h) * exp(-1 / (2 * h) * ((x(i) - r(j)) ^ 2));
        end
        temp = temp / 1000;
        y(i) = temp;
    end
    plot(x, y);
    title(['h = ',num2str(h)]);
    h = h / 10;
end