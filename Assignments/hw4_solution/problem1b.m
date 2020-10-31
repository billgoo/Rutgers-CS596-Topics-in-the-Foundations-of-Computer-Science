r = rand(1000, 1);
r = transpose(r);
x = [-2:0.004:1.996];
h = 1;
while h > 1e-6
    y = [];
    for i = 1:1000
        temp = 0;
        for j = 1:1000
            temp = temp + 1 / (2 * h) * exp(-1 / h * abs(x(i) - r(j)));
        end
        temp = temp / 1000;
        y(i) = temp;
    end
    plot(x, y);
    title(['h = ',num2str(h)]);
    h = h / 10;
end