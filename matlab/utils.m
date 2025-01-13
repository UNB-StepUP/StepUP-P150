classdef utils
    properties (Constant)
        dataset_folder = '/home/shared/stepUP-P150/mat'; % path to local data folder
    end
    methods(Static)
        function metadata = load_metadata(participant_id, footwear, speed)
            f = fullfile(utils.dataset_folder, sprintf('%03.0f',participant_id),footwear,speed,'metadata.csv');
            metadata = readtable(f);
        end

        function trial = load_trial(participant_id, footwear, speed)
            f = fullfile(utils.dataset_folder, sprintf('%03.0f',participant_id),footwear,speed,'trial.mat');
            trial = load(f).arr_0;
        end

        function  footsteps = load_footsteps(participant_id, footwear, speed, pipeline)
            if nargin < 3
                pipeline = 1; % load pipeline 1 footsteps by default
            end
            f = fullfile(utils.dataset_folder, sprintf('%03.0f',participant_id),footwear,speed,sprintf('pipeline_%d.mat',pipeline));
            footsteps = load(f).arr_0;
        end

    end
end

