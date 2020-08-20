<!DOCTYPE html>

<link href="https://fonts.googleapis.com/css2?family=Fondamento&family=Open+Sans&display=swap" rel="stylesheet">
<!--
TODO:
    - load styles from file
    - use constants for character sheet headers
-->
<style>
    :root {
        --color-bg: #086375;
        --color-fg: #EFEFEF;
        --color-textbox-bg: #08353E;
        --color-details-fg: #49A078;
    }


    .character_sheet h1, .character_sheet h2, .character_sheet h3,
    .character_sheet h4, .character_sheet h5, .character_sheet h6 {
        font-family: 'Fondamento', cursive !important;
        color: white !important;
        line-height: 1em !important;
    }

    .character_sheet {
        width: 100%;
        display: inline-flex;
        float: left;

        line-height: normal;
    }

    .column {
        border-radius: 5px;
        overflow: hidden;

        margin: 5px;

        background-color: var(--color-bg);
        color: var(--color-fg);

        -moz-box-shadow: 0 0 25px #333333;
        -webkit-box-shadow:0 0 25px #333333;
        box-shadow: 0 0 25px #333333;

        font-family: 'Open Sans', sans-serif;
        font-size: 12px;
    }

    .column p {
        margin: 0 0 2px;
    }

    .column strong {
        color: white;
    }

    .character_basic_info {
        display: block;
        padding: 0 10px 10px;
    }

    .character_sheet hr {
        border: 0 !important;
        border-top: 3px solid var(--color-details-fg) !important;
        margin: 10px 0 !important;
        clear:both !important;
        display:block !important;
    }

    .left_column {
        width: 33%;
        float: left;
        position: relative;
    }

    .right_column {
        width: 67%;

        float: left;
        position: relative;

        padding: 10px;

        display: inline-flex;
    }

    .display_bottomleft {
        position: absolute;
        width: 100%;
        left: 0;
        bottom: 0;

        padding: 0 0 0 10px;

        color: white;
        text-shadow: 1px 1px black;
    }

    .logo_13thage {
        position: absolute;
        top: 0;
        right: 0;
    }

    .logo_13thage img {
        width: 32px;
        height: 32px;

        border-radius: 0 0 0 2px;
    }


    .character_portrait_container {
        max-height: 250px;
        overflow: hidden;
        position: relative;
    }

    .ability_scores {
        float: left;
        position: relative;
        margin: 0 auto;
        width: 16.66666667%;
    }

    .ability_scores p, .ability_scores strong {
        text-align: center !important;
        text-transform: uppercase;
    }

    .textbox {
        background-color: var(--color-textbox-bg);
        border-radius: 5px;
        padding: 5px;
    }

    .textbox strong {
        font-family: 'Fondamento', serif;
    }

    .icons_relationships {
        font-size: 14px;
    }

    .right_column_right_container, .right_column_left_container {
        width: 50%;
        float: left;
    }

    .right_column_left_container {
        padding-right: 10px;
    }

    .right_column_right_container {
        padding-left: 10px;
    }

    .feat {
        padding-left: 10px;
        background: var(--color-textbox-bg);
        background: linear-gradient(90deg, var(--color-textbox-bg) 0%, var(--color-bg) 50%, var(--color-textbox-bg) 100%);
    }
</style>

<%!
    from templates_helper.images import embed_image
    import constants.user_interface as ui_constants
%>



<!-- check if the feat_list is not empty then print them in the right div -->
<%def name="feats_block(feat_list)">
% if feat_list:
        % for feat in feat_list:
            <p class="feat"><strong>${feat.type}:</strong> ${feat.description}</p>
        % endfor
% endif
</%def>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>13th Age Character Sheet</title>
</head>

<body>

<!-- the object we are going to represent is stored in the character var accessible trough ${character} -->
<div class="character_sheet">
    <div class="left_column column">

        <div class="character_portrait_container">

            <img src="${embed_image(character.picture_path)}" style="width: 100%" alt="Character Portrait">
            <div class="display_bottomleft">
                <h1>${character.name}</h1>
                <p>Level ${character.level} ${character.race_name} ${character.class_name}, Pure Neutral</p>
            </div>

            <div class="logo_13thage">
                <img src="${embed_image(ui_constants.ICON_13THAGE_LOGO)}" alt="13th Age Logo">
            </div>

        </div>

        <div class="character_basic_info">
            <hr>

            <div>
                <p><strong>Armor Class: </strong>${character.ac}</p>
                <p><strong>Physical Defence: </strong>${character.pd}</p>
                <p><strong>Mental Defence: </strong>${character.md}</p>
                <p><strong>Hit Points: </strong>${character.hp} (${character.hp_max})</p>
                <p><strong>Recoveries: </strong>
                    ${character.recoveries}${character.recovery_die} (${character.recoveries}${character.recovery_die})
                </p>
            </div>

            <hr>

            % for ability_score in character.ability_scores:
            <div class="ability_scores">
                <p><strong>${ability_score.name[:3]}</strong></p>
                <p>${ability_score.value} (${"{0:+}".format(ability_score.get_modifier())})</p>
                <p>${"{0:+}".format(ability_score.get_modifier() + character.level)}</p>
            </div>
            % endfor

            <hr>

            <div>
                <p>
                    <strong>Backgrounds:</strong>
                    <!--
                    index is needed to check if the background is
                    the last in the tuple, so we can append a commas
                    to values that are not the last
                    -->
                    % for background, index in zip(character.backgrounds, range(len(character.backgrounds))):
                    <i>${background.name}</i>
                        % if index != len(character.backgrounds)-1:
                            ${" {0:+},".format(background.value)}
                        % else:
                            ${" {0:+}".format(background.value)}
                        % endif
                    % endfor
                </p>
            </div>

            <hr>

            <div class="textbox">
                <p><strong>One Unique Thing</strong></p>
                <p>${character.out}</p>
            </div>

        </div>
    </div>

    <div class="right_column column">
        <div class="right_column_left_container">

            % if character.racial_power:
            <div class="race_powers">
                <h2>Racial Powers</h2>

                <div class="textbox">
                    <strong>${character.racial_power.name}</strong>
                    <p>${character.racial_power.description}</p>
                    ${feats_block(character.racial_power.feats)}
                </div>
            </div>
            <hr>
            % endif

            % if character.class_features:
            <div class="features">
                <h2>Class Features</h2>

                % for class_feature in character.class_features:
                <div class="textbox">
                    <strong>${class_feature.name}</strong>
                    <p>${class_feature.description}</p>
                    ${feats_block(class_feature.feats)}
                </div><br>
                % endfor
            </div>
            <hr>
            % endif

            % if character.class_talents:
            <div class="talents">
                <h2>Class Talents</h2>

                % for class_talent in character.class_talents:
                <div class="textbox">
                    <strong>${class_talent.name}</strong>
                    <p>${class_talent.description}</p>
                    ${feats_block(class_talent.feats)}
                </div><br>
                % endfor

            </div>
            % endif
        </div>

        <div class="right_column_right_container">

            % if character.powers_and_spells:
            <div class="features">
                <h2>Class Features</h2>

                % for power in character.powers_and_spells:
                <div class="textbox">
                    <strong>${power.name}</strong>
                    <p>${power.description}</p>
                    ${feats_block(power.feats)}
                </div><br>
                % endfor
            </div>
            <hr>
            % endif


            % if character.icon_relationships:
            <div class="icons_relationships">
                <h2>Icon Relationships</h2>
                % for icon_relationship in character.icon_relationships:
                <p><strong>${icon_relationship.name}: </strong>${icon_relationship.type}</p>
                % endfor
            </div>
            % endif

        </div>
    </div>
</div>
</body>
</html>