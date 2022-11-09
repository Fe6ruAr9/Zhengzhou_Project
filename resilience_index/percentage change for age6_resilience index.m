
clear;

%%
clc;

%%
%%c
%c2(1,:)=[];
%%
%%c
x1=c2(:,1);
x1=table2array(x1);
y1=c2(:,2);
y1=table2array(y1);
%%
y1=y1*100
%%
% %%
% figure
% p=plot(x1,y1,'-o','MarkerSize',2,'MarkerEdgeColor','#DF9298','MarkerFaceColor','#DF9298');
% %p.Marker = ('o','MarkerSize',1);
% xlim([0 408]);
% xticks(0:24:408);
% set(gca,'xtick',[0 24 48 72 96 120 144 168 192 216 240 264 288 312 336 360 384],'xticklabels',{'07/13','07/14','07/15','07/16','07/17','07/18','07/19','07/20','07/21','07/22','07/23','07/24','07/25','07/26','07/27','07/28','07/29',})
% %set(gca,'xtick',[0 24 48 72 96 120 144 168 192 216 240 264 288 312 336 360 384],'xticklabels',{'07/13 00:00','07/14 00:00','07/15 00:00','07/16 00:00','07/17 00:00','07/18 00:00','07/19 00:00','07/20 00:00','07/21 00:00','07/22 00:00','07/23 00:00','07/24 00:00','07/25 00:00','07/26 00:00','07/27 00:00','07/28 00:00','07/29 00:00',})
% ylabel('Percentage Change(%)','FontSize',17);
% xlabel('Time','FontSize',17);
% %xlabel('Successive Hours from July13 to July 29','FontSize',17);

%%

figure
windowSize = 24; 
b = (1/windowSize)*ones(1,windowSize);
a = 1;

%%画bar的真值。
y2 = filter(b,a,y1);
bar(x1,y1);
%%画average smooth的值。
hold on
plot(x1,y2,'k--','lineWidth',2);

%%画average smooth那一条线的把y>0的那些y值变成0.
y2_1=y2;

for i=1:1:size(y2_1,1)
    if y2_1(i,1)>0
        y2_1(i,1)=0;
    end
end

%%限定范围是在灾中的20号即第168个小时开始。画出那条我需要计算area under curve面积的曲线范围。
x2=x1(168:end);
y2_2=y2_1(168:end);
hold on 
plot(x2,y2_2,'-','Color','#DF9298','LineWidth',4);

hl=legend('Percentage Change of Total Flux Per Hour','Moving Average (WindowSize = 24)','Performance During and After Event','Location','Northeast','FontSize',17);
set(hl,'Box','off');
%%
xlim([0 408]);
ylim([-150 150]);
xticks(0:24:408);
set(gca,'xtick',[0 24 48 72 96 120 144 168 192 216 240 264 288 312 336 360 384],'xticklabels',{'07/13','07/14','07/15','07/16','07/17','07/18','07/19','07/20','07/21','07/22','07/23','07/24','07/25','07/26','07/27','07/28','07/29',})
%set(gca,'xtick',[0 24 48 72 96 120 144 168 192 216 240 264 288 312 336 360 384],'xticklabels',{'07/13 00:00','07/14 00:00','07/15 00:00','07/16 00:00','07/17 00:00','07/18 00:00','07/19 00:00','07/20 00:00','07/21 00:00','07/22 00:00','07/23 00:00','07/24 00:00','07/25 00:00','07/26 00:00','07/27 00:00','07/28 00:00','07/29 00:00',})
ylabel('Percentage Change(%)','FontSize',17);
xlabel('Time','FontSize',17);
title(['W>=100 - RI=0.40'],'Fontsize',17)
%xlabel('Successive Hours from July13 to July 29','FontSize',17);

%%
%y3=0

%trapz(x1,y3);

area=trapz(x2,y2_2);

%% normalizing y2_2 to 0-1

y2_3=(y2_2-min(y2_2))./abs(min(y2_2));
x3=[1:1:size(y2_3)];
figure
plot(x3,y2_3);

%% 算那个resilience index 的值。
area2=trapz(x3,y2_3);
area0=1*max(x3);
resindex=area2/area0;
%ylim([0 1.5]);