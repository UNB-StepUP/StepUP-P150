%% Select Trial

participant_id = 37; % possible values: integers from 1 - 150
shoe_type = 'ST'; % possible values: 'BF', 'ST', 'P1', 'P2'
walk_condition = 'W3'; % possible values: 'W1', 'W2', 'W3', 'W4'

%% Load Footstep Metadata

metadata = utils.load_metadata(participant_id,shoe_type,walk_condition);
disp(metadata)

%% Load Raw Trial Recording

trial = utils.load_trial(participant_id,shoe_type,walk_condition);

disp(['Tensor size (frames, height, width): ',num2str(size(trial))])

% visualize data 
figure
cmap = colormap('jet');
cmap(1,:) = [0,0,0];

% display all passes on tiles
subplot(2,1,1)
img_peak = squeeze(max(trial,[],1));
img_peak = rot90(img_peak);
imagesc(img_peak)
colormap(cmap)
axis('equal')
axis('off')
title('Peak Pressures from Entire 90-Second Recording')

% display one pass across tiles
subplot(2,1,2)
iPass = 5;
pass_idx = find(metadata.PassID == iPass);
start_t = metadata.StartFrame(pass_idx(1)) + 1;
end_t = metadata.EndFrame(pass_idx(end)) + 1;
img_peak = squeeze(max(trial(start_t:end_t,:,:),[],1));
img_peak = rot90(img_peak);
imagesc(img_peak)
colormap(cmap)
axis('equal')
axis('off')
title('Peak Pressures from One Pass')

%% Load Extracted Footsteps (Pipeline 1)

footsteps = utils.load_footsteps(participant_id, shoe_type, walk_condition,1);
disp(['Tensor size (n_steps, frames, height, width):',num2str(size(footsteps))])

% remove outlier and partial footsteps 
footsteps = footsteps(metadata.Exclude == false,:,:,:);

% plot the peak pressures for the first 12 steps
figure
for iFootstep = 1:12
    subplot(3,4,iFootstep)
    footstep = footsteps(iFootstep,:,:,:);
    img_peak = squeeze(max(footstep,[],2));
    imagesc(img_peak)
    colormap(cmap)
    axis('equal')
    axis('off')
end
sgtitle('Peak Pressures for Example Extracted Footsteps')
